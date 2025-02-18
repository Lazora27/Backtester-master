import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MassIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MassIndex': 1.0
        })
    )
