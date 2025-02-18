import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und WilliamsR
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'WilliamsR': 1.0
        })
    )
