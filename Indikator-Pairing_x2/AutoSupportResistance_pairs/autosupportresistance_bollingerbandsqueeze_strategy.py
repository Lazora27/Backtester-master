import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
