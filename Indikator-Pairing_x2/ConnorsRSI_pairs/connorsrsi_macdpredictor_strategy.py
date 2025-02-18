import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MACDPredictor': 1.0
        })
    )
