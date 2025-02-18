import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'AccelerationBands': 1.0
        })
    )
