import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
