import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
