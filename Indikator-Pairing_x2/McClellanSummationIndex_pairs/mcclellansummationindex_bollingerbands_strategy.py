import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
