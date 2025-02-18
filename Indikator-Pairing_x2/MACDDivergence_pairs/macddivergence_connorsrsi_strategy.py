import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'ConnorsRSI': 1.0
        })
    )
