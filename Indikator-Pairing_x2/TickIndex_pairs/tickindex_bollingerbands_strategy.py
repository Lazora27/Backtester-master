import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
