import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
