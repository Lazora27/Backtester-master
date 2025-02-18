import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
