import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'AccelerationBands': 1.0
        })
    )
