import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
