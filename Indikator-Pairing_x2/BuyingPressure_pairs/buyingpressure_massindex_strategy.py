import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und MassIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'MassIndex': 1.0
        })
    )
