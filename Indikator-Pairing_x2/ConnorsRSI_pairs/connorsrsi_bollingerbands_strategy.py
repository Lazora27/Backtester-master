import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'BollingerBands': 1.0
        })
    )
