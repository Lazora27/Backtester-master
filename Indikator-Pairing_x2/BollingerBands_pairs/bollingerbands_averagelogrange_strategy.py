import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'AverageLogRange': 1.0
        })
    )
