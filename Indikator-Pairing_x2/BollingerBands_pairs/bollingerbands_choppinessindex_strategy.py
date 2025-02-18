import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
