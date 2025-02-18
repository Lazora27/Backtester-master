import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'BradleySiderograph': 1.0
        })
    )
