import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'TRIXIndicator': 1.0
        })
    )
