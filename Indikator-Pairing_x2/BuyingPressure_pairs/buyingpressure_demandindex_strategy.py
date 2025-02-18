import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und DemandIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'DemandIndex': 1.0
        })
    )
