import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
