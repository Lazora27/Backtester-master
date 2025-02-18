import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CCITurbo
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CCITurbo': 1.0
        })
    )
