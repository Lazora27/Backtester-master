import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und BollingerBands
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'BollingerBands': 1.0
        })
    )
