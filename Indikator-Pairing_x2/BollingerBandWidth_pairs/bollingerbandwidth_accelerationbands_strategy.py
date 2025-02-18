import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'AccelerationBands': 1.0
        })
    )
