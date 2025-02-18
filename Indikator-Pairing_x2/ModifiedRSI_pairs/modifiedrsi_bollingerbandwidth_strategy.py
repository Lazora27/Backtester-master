import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
