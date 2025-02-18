import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
