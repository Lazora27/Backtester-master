import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
