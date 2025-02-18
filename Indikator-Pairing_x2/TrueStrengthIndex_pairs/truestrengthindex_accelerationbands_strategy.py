import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
