import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'CCITurbo': 1.0
        })
    )
