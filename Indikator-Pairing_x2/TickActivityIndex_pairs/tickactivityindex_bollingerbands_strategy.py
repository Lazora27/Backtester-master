import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
