import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
