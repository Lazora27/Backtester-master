import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AccelerationBands': 1.0
        })
    )
