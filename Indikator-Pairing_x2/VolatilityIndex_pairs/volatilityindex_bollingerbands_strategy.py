import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
