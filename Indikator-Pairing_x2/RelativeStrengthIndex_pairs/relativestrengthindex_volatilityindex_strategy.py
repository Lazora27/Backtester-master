import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
