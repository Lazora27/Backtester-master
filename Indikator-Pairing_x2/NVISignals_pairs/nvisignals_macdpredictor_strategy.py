import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MACDPredictor': 1.0
        })
    )
