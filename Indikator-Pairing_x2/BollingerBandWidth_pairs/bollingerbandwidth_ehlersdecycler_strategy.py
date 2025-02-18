import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'EhlersDecycler': 1.0
        })
    )
