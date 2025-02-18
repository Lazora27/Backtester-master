import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'OpenInterest': 1.0
        })
    )
