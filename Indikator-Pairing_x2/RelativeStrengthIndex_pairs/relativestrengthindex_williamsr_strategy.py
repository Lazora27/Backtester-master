import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
