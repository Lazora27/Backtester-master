import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'BradleySiderograph': 1.0
        })
    )
