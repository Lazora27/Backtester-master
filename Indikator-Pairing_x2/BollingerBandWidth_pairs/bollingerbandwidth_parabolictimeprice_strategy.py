import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
