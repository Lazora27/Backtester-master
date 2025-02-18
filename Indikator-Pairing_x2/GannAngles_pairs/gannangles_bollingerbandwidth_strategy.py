import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
