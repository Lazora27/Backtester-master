import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
