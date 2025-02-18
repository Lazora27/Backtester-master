import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DPOCycles': 1.0
        })
    )
