import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
