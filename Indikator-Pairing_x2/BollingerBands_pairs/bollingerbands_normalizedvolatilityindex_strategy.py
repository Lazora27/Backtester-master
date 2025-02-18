import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_NormalizedVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und NormalizedVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'NormalizedVolatilityIndex': 1.0
        })
    )
