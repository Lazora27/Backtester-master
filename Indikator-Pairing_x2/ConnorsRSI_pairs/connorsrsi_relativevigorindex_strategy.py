import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
