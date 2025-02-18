import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BollingerBands': 1.0
        })
    )
