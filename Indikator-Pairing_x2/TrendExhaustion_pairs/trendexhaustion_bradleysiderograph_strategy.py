import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'BradleySiderograph': 1.0
        })
    )
