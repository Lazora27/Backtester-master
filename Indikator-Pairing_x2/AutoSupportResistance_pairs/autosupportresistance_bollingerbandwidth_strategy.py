import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
