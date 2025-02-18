import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
