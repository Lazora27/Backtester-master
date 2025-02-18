import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BollingerBands
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BollingerBands': 1.0
        })
    )
