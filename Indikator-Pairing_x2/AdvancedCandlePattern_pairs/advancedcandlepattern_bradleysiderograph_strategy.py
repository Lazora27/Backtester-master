import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'BradleySiderograph': 1.0
        })
    )
