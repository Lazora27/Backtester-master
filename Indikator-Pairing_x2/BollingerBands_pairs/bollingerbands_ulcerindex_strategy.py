import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'UlcerIndex': 1.0
        })
    )
