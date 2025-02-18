import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
